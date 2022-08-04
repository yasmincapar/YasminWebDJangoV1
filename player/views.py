from django.shortcuts import render,get_object_or_404
from .models import PlayerModel

def playerlist(request):
    #bilgiler = [{'title': 'Player Listesi', 'content': 'Player Listesi'},{'title': 'player Listesi 2', 'content': 'player Listesi 2'}]
    ##bilgiler={'name':'the player list','surname':'the player list'}
    #bilgiler=[{'name':'the player list','surname':'the player list'}]
    bilgiler=PlayerModel.objects.all()
    #in jason format
    return render(request,'player/playerlist.html',{"players":bilgiler})
    #musteriden istek gelir http
   # {"players":bilgiler} i send data with this line 

def playerdetail(request,pk):
    #404 sayfa bulunamadi 
    player=get_object_or_404(PlayerModel,pk=pk)
    return render(request, 'player/playerdetail.html',{"player":player})
    #we get the player detail from the database


