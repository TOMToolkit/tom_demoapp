from django import template
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

from tom_demoapp import __version__
from tom_demoapp.models import DemoProfile

register = template.Library()


@register.inclusion_tag('tom_demoapp/partials/profile_demo.html')
def demo_profile_data(user):
    """
    Returns the app specific user information as a dictionary to be used in the context of the above partial.
    """

    # demo_secret is rendered separately via tom_common's revealable_password_input
    # partial, so exclude it from the auto-iteration loop. model_to_dict goes
    # through EncryptedModelField.value_from_object, which returns the REDACTED
    # placeholder string for security; the partial needs the actual plaintext,
    # which only direct attribute access provides.
    exclude_fields = ['user', 'id', 'demo_secret']
    try:
        demo_profile_dict = model_to_dict(user.demoprofile, exclude=exclude_fields)
        return {
            'user': user,
            'demo_profile': user.demoprofile,
            'demo_profile_data': demo_profile_dict,
            'demo_secret': user.demoprofile.demo_secret,  # direct access → plaintext
            'version': __version__,  # from tom_demoapp/__init__.py
        }
    except DemoProfile.DoesNotExist:
        DemoProfile.objects.create(user=user)
        return {'user': user,
                'demo_profile': user.demoprofile,
                'demo_profile_data': {},
                'demo_secret': user.demoprofile.demo_secret,
                'version': __version__}  # from tom_demoapp/__init__.py


@register.inclusion_tag('tom_demoapp/partials/demo_user_list.html', takes_context=True)
def demo_user_list(context):
    """
    Returns the app specific user information as a dictionary to be used in the context of the above partial.
    """

    users = User.objects.filter(username__startswith='A')
    context = {'users': users}
    return context


@register.inclusion_tag('tom_demoapp/partials/demo_button.html', takes_context=True)
def demo_button(context):
    """
    Returns the app specific context for making a target detail button.
    """

    context = {'button_text': 'Demo App'}
    return context
