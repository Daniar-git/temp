from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from metamask_auth.decorators import has_ethereum_address


@login_required
@has_ethereum_address
def my_view(request):
    ethereum_address = request.user.ethereum_address
    username = request.user.username
    email = request.user.email
    print("Yes")

    return JsonResponse({'success': True})