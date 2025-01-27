from django import template
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

from tom_demoapp.models import DemoProfile

register = template.Library()


@register.inclusion_tag('tom_demoapp/partials/profile_demo.html')
def demo_profile_data(user):
    """
    Returns the app specific user information as a dictionary to be used in the context of the above partial.
    """

    exclude_fields = ['user', 'id']
    try:
        demo_profile_dict = model_to_dict(user.demoprofile, exclude=exclude_fields)
        demo_profile_dict['demo_secret'] = "**************"
        return {
            'user': user,
            'demo_profile': user.demoprofile,
            'demo_profile_data': demo_profile_dict,
        }
    except DemoProfile.DoesNotExist:
        DemoProfile.objects.create(user=user)
        return {'user': user,
                'demo_profile': user.demoprofile,
                'demo_profile_data': {}}


@register.inclusion_tag('tom_demoapp/partials/demo_user_list.html', takes_context=True)
def demo_user_list(context):
    """
    Returns the app specific user information as a dictionary to be used in the context of the above partial.
    """

    users = User.objects.filter(username__startswith='A')
    context = {'users': users}
    return context
