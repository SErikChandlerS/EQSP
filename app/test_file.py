import pytest    
from app.models import Contact  
from app.views import contact_list_view 
from django.urls import reverse, resolve
from django.test import RequestFactory


@pytest.mark.django_db
def test_view():
    path = reverse("contact_list")
    request = RequestFactory().get(path)
    response = contact_list_view(request)

    assert response.status_code == 200


@pytest.mark.django_db    
def test_contact_create():
    contact = Contact.objects.create(full_name="Erik Chandler", phone_number="79920241320", description="dfsdfsdfsdf")

    assert contact.full_name == "Erik Chandler"
    assert contact.phone_number == "79920241320"
    assert contact.phone_number == "dfsdfsdfsdf"


def test_url():            
    path = reverse('contact_list')

    assert resolve(path).view_name == "contact_list"


