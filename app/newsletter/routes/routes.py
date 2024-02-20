from flask import Blueprint, request, jsonify

from app.newsletter.application.services import EmailService
from app.shared import exceptions

newsletter_bp = Blueprint("newsletter", __name__)


@newsletter_bp.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World"})


@newsletter_bp.route("/create", methods=["POST"])
def create_campaign():
    try:
        data = request.json
        name = data.get("name")
        description = data.get("description")
        category = data.get("category")
        subject = data.get("subject")
        html_content = data.get("html")
        recipients_emails = data.get("emails")
        campaign = EmailService.create_campaign(name, description, category, subject, html_content)
        EmailService.create_recipients(recipients_emails)
        EmailService.add_recipient_to_campaign(campaign.id, recipients_emails)
        return jsonify({"message": "Campaign created successfully"})
    except exceptions.ServiceNotAvaliableError as e:
        return jsonify({"message": str(e)}, 503)
    except Exception as e:
        return jsonify({"message": str(e)})


@newsletter_bp.route("/campaigns", methods=["GET"])
def get_campaigns():
    try:
        campaigns = EmailService.get_campaigns()
        serialized_campaigns = [
            {
                "id": campaign.id,
                "name": campaign.name,
                "description": campaign.description,
                "category": campaign.category,
                "subject": campaign.subject,
                "html_content": campaign.html_content,
            }
            for campaign in campaigns
        ]
        return jsonify({"data": serialized_campaigns})
    except exceptions.CampaignNotFound as e:
        return jsonify({"message": str(e)}, 404)
    except Exception as e:
        return jsonify({"message": str(e)})

@newsletter_bp.route("/send/<campaign_id>", methods=["POST"])
def send_campaign(campaign_id):
    try:
        EmailService.send_campaign(campaign_id)
        return jsonify({"message": "Campaign sent successfully"})
    except exceptions.CampaignNotFound as e:
        return jsonify({"message": str(e)}, 404)
    except exceptions.RecipientNotFound as e:
        return jsonify({"message": str(e)}, 404)
    except Exception as e:
        return jsonify({"message": str(e)})


@newsletter_bp.route("/unsubscribe/<email>", methods=["POST"])
def unsubscribe(email):
    updated_recipient = EmailService.unsubscribe(email)
    return jsonify({"message": "Unsubscribed successfully", "data": updated_recipient.email})
