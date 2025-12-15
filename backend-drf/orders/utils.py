from django.core.mail import send_mail
from django.conf import settings

def send_order_notification(order):
    send_mail(
        subject=f"Order #{order.id} is recieved",
        message=f"""
            Hi {order.user.first_name} {order.user.last_name}

            Your Order ${order.id} has been placed successfully.

            Total: {order.grand_total}

            Thank you for Shopping with ClickMart.

            We will meet again!!!
        """,
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=[order.user.email],
        fail_silently=False
    )