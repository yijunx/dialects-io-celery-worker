from celery import Celery
from app.app_config import conf
from app.services.email_handler import send_email_verification


app = Celery(conf.SERVICE_NAME, broker=conf.BROKER)


@app.task()
def email_confirmation(
    token: str, user_email: str, user_name: str  # job_id: str
):
    send_email_verification(token=token, user_email=user_email, user_name=user_name)


@app.task()
def update_user_info(
    user_id: str, user_name: str = None, user_email: str = None  # ob_id: str, 
):
    print("updating use info")
    pass


if __name__ == "__main__":
    app.worker_main(
        argv=[
            "worker",
            f"--autoscale={conf.WORKER_MAX},{1}",
            f"--loglevel=info",
            "--queues",
            conf.QUEUE,


        ]
    )