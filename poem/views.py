import openai
from openai import OpenAI
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poem, Appreciation

client = OpenAI(
    api_key=settings.OPENAI_API_KEY,
    organization = 'org-wdtq1hh5ebP27YnKDDVtLvdU'
)

def poem_detail(request, poem_id):
    poem = get_object_or_404(Poem, id=poem_id)
    appreciations = Appreciation.objects.filter(poem=poem).order_by('-created_at') # 최신순 정렬
    return render(request, 'poem/poem_detail.html', {'poem': poem, 'appreciations': appreciations})

def generate_appreciation(request, poem_id):
    poem = get_object_or_404(Poem, id=poem_id)

    prompt_text = f"""
    제목: {poem.title}
    작가: {poem.author}
    내용:
    {poem.content}

    이 시를 감상한 짧은 감상문을 10자 이내로 써주세요.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 시 감상문을 작성하는 문학 전문가입니다."},
                {"role": "user", "content": prompt_text}
            ],
            temperature=0.7,
            max_tokens=300
        )
        generated_text = response.choices[0].message.content.strip()

        # 생성된 감상문을 DB에 저장
        Appreciation.objects.create(
            poem=poem,
            content=generated_text
        )

        return JsonResponse({'appreciation': generated_text})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

