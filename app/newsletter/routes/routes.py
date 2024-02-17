from flask import Blueprint, request, jsonify

from app.newsletter.application.services import EmailService

newsletter_bp = Blueprint("newsletter", __name__)


@newsletter_bp.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World"})

@newsletter_bp.route("/create", methods=["POST"])
def create_campaign():
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