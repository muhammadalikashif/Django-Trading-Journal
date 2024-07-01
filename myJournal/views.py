from django.shortcuts import redirect, render
from .forms import  TradeForm
from .models import Trade
from django.views.generic import ListView
# Create your views here.


from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

@login_required  # Ensure the user is logged in to access this view
def index(request):
    if request.method == 'POST':
        form = TradeForm(request.POST, request.FILES)
        if form.is_valid():
            trade = form.save(commit=False)
            
            # Set the user associated with this trade
            trade.custom_user = request.user  # Assuming you have a user object in your request
            
            if trade.exit_price is not None and trade.entry_price is not None:
                if trade.position == 'Long':
                    if trade.exit_price > trade.entry_price:
                        trade.result = 'Win'
                        trade.profit_loss = ((trade.exit_price - trade.entry_price) / float(trade.entry_price)) * 100
                    elif trade.exit_price < trade.entry_price:
                        trade.result = 'Loss'
                        trade.profit_loss = ((trade.exit_price - trade.entry_price) / float(trade.entry_price)) * 100
                    else:
                        trade.result = 'Break Even'
                        trade.profit_loss = 0
                elif trade.position == 'Short':
                    if trade.exit_price > trade.entry_price:
                        trade.result = 'Loss'
                        trade.profit_loss = ((trade.entry_price - trade.exit_price) / float(trade.entry_price)) * 100
                    elif trade.exit_price < trade.entry_price:
                        trade.result = 'Win'
                        trade.profit_loss = ((trade.entry_price - trade.exit_price) / float(trade.entry_price)) * 100
                    else:
                        trade.result = 'Break Even'
                        trade.profit_loss = 0
                else:
                    trade.result = ''
                    trade.profit_loss = 0
            else:
                trade.result = ''
                trade.profit_loss = None
                # ... Rest of your logic ...

            trade.save()
            return redirect('profile')
    else:
        form = TradeForm()

    trades = Trade.objects.all()
    return render(request, 'myJournal/index.html', {'form': form, 'trades': trades})

'''
@login_required
def index(request):
    if request.method == 'POST':
        form = TradeForm(request.POST, request.FILES)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.user = request.user  # Associate the trade with the current user
            # ... your existing logic ...
            if trade.exit_price is not None and trade.entry_price is not None:
                if trade.position == 'Long':
                    if trade.exit_price > trade.entry_price:
                        trade.result = 'Win'
                        trade.profit_loss = ((trade.exit_price - trade.entry_price) / float(trade.entry_price)) * 100
                    elif trade.exit_price < trade.entry_price:
                        trade.result = 'Loss'
                        trade.profit_loss = ((trade.exit_price - trade.entry_price) / float(trade.entry_price)) * 100
                    else:
                        trade.result = 'Break Even'
                        trade.profit_loss = 0
                elif trade.position == 'Short':
                    if trade.exit_price > trade.entry_price:
                        trade.result = 'Loss'
                        trade.profit_loss = ((trade.entry_price - trade.exit_price) / float(trade.entry_price)) * 100
                    elif trade.exit_price < trade.entry_price:
                        trade.result = 'Win'
                        trade.profit_loss = ((trade.entry_price - trade.exit_price) / float(trade.entry_price)) * 100
                    else:
                        trade.result = 'Break Even'
                        trade.profit_loss = 0
                else:
                    trade.result = ''
                    trade.profit_loss = 0
            else:
                trade.result = ''
                trade.profit_loss = None
            trade.save()
            return redirect('index')
    else:
        form = TradeForm()

    trades = Trade.objects.filter(user=request.user)  # Filter trades by the current user
    return render(request, 'myJournal/index.html', {'form': form, 'trades': trades})

'''

'''
def index(request):
    if request.method == 'POST':
        form = TradeForm(request.POST, request.FILES)
        if form.is_valid():
            trade = form.save(commit=False)
            
            if trade.exit_price is not None and trade.entry_price is not None:
                if trade.position == 'Long':
                    if trade.exit_price > trade.entry_price:
                        trade.result = 'Win'
                        trade.profit_loss = ((trade.exit_price - trade.entry_price) / float(trade.entry_price)) * 100
                    elif trade.exit_price < trade.entry_price:
                        trade.result = 'Loss'
                        trade.profit_loss = ((trade.exit_price - trade.entry_price) / float(trade.entry_price)) * 100
                    else:
                        trade.result = 'Break Even'
                        trade.profit_loss = 0
                elif trade.position == 'Short':
                    if trade.exit_price > trade.entry_price:
                        trade.result = 'Loss'
                        trade.profit_loss = ((trade.entry_price - trade.exit_price) / float(trade.entry_price)) * 100
                    elif trade.exit_price < trade.entry_price:
                        trade.result = 'Win'
                        trade.profit_loss = ((trade.entry_price - trade.exit_price) / float(trade.entry_price)) * 100
                    else:
                        trade.result = 'Break Even'
                        trade.profit_loss = 0
                else:
                    trade.result = ''
                    trade.profit_loss = 0
            else:
                trade.result = ''
                trade.profit_loss = None
            
            trade.save()
            return redirect('index')
    else:
        form = TradeForm()

    trades = Trade.objects.all()
    return render(request, 'myJournal/index.html', {'form': form, 'trades': trades})
'''
@login_required
def my_trades_view(request):
    # Filter trades by the logged-in user
    trades = Trade.objects.filter(custom_user=request.user)

    return render(request, 'myJournal/my_trades.html', {'trades': trades})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout