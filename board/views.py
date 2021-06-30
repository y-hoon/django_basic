from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect

from tag.models import Tag
from .models import Board
from .forms import BoardForm
from user.models import User


# create your views here.

def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'board_detail.html', {'board': board})


def board_list(request):
    boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(boards, 3)
    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/user/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            tags = form.cleaned_data['tags'].split(',')

            for tag in tags:
                if not tag:
                    continue

                # 태그가 존재하면 아무 동작하지 않고 존재하지 않으면 생성함
                _tag, created = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})
