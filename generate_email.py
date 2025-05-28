from jinja2 import Template

def generate_email(data):
    plain_template = """
Dear {{ name }},

Greetings from the KIIT E-Cell!

KIIT University's Entrepreneurship Cell is thrilled to announce {{ event_name }}, a premier entrepreneurship event under the theme
"{{ event_theme }}." This flagship summit aims to inspire, empower, and connect aspiring entrepreneurs and industry leaders from across the nation.
The event is tentatively scheduled for {{ event_dates }}, and we cordially invite you to join us as a distinguished speaker.

Established in 1992 by Dr. Achyuta Samanta, the {{ institute_name }} has grown into a premier institution known for its innovation and academic excellence. With a vibrant community of {{ student_count }} students and faculty members, KIIT continues to set benchmarks in education and research. Additionally, the {{ social_institute }} stands as a unique initiative, providing holistic care and education to {{ social_student_count }} tribal students from nursery through post-graduation, empowering marginalized communities and fostering inclusive growth.

{% for paragraph in custom_paragraphs %}
{{ paragraph }}

{% endfor %}

{{ event_name }} is a distinguished platform designed to foster entrepreneurial spirit and innovation among youth. With participation from thousands of students, industry experts, and startups, it offers a dynamic environment to exchange ideas, showcase innovation, and nurture leadership qualities essential for creating sustainable and impactful ventures. The summit annually attracts {{ expert_count }} experts and entrepreneurs, creating lasting networks and opportunities for growth and collaboration.

We would be honored to have you deliver a keynote address at our speaker session during {{ event_name }}. The travel fare and accommodation will be arranged and provided by us. We have attached the brochure for your reference. Should you be available, we would be happy to share more details and explore how your expertise can contribute to the event’s vision and success.

Your presence will significantly enhance the experience for everyone and leave a meaningful impact on all attendees.

Thank you for considering this invitation. We look forward to your positive response.

Warm Regards,
{{ contact_name }}
{{ contact_role }}
Contact No.: {{ contact_phone }}
Entrepreneurship Cell, KIIT University
"""

    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Invitation Email</title>
<style>
  body { font-family: Arial, sans-serif; color: #333; line-height: 1.6; }
  .container { max-width: 650px; margin: auto; padding: 20px; border: 1px solid #ddd; background: #fff; }
  p { margin-bottom: 16px; }
  .signature { margin-top: 30px; }
</style>
</head>
<body>
<div class="container">
  <p>Dear <strong>{{ name }}</strong>,</p>

  <p>Greetings from the KIIT E-Cell!</p>

  <p>KIIT University's Entrepreneurship Cell is thrilled to announce <strong>{{ event_name }}</strong>, a premier entrepreneurship event under the theme  
  "<em>{{ event_theme }}</em>." This flagship summit aims to inspire, empower, and connect aspiring entrepreneurs and industry leaders from across the nation.  
  The event is tentatively scheduled for <strong>{{ event_dates }}</strong>, and we cordially invite you to join us as a distinguished speaker.</p>

  <p>Established in 1992 by Dr. Achyuta Samanta, the {{ institute_name }} has grown into a premier institution known for its innovation and academic excellence.  
  With a vibrant community of {{ student_count }} students and faculty members, KIIT continues to set benchmarks in education and research. Additionally, the {{ social_institute }} stands as a unique initiative, providing holistic care and education to {{ social_student_count }} tribal students from nursery through post-graduation, empowering marginalized communities and fostering inclusive growth.</p>

  {% for paragraph in custom_paragraphs %}
  <p>{{ paragraph }}</p>
  {% endfor %}

  <p>{{ event_name }} is a distinguished platform designed to foster entrepreneurial spirit and innovation among youth. With participation from thousands of students, industry experts, and startups, it offers a dynamic environment to exchange ideas, showcase innovation, and nurture leadership qualities essential for creating sustainable and impactful ventures.  
  The summit annually attracts {{ expert_count }} experts and entrepreneurs, creating lasting networks and opportunities for growth and collaboration.</p>

  <p>We would be honored to have you deliver a keynote address at our speaker session during {{ event_name }}. The travel fare and accommodation will be arranged and provided by us. We have attached the brochure for your reference. Should you be available, we would be happy to share more details and explore how your expertise can contribute to the event’s vision and success.</p>

  <p>Your presence will significantly enhance the experience for everyone and leave a meaningful impact on all attendees.</p>

  <p>Thank you for considering this invitation. We look forward to your positive response.</p>

  <div class="signature">
    <p>Warm Regards,<br />
    {{ contact_name }}<br />
    {{ contact_role }}<br />
    Contact No.: {{ contact_phone }}<br />
    Entrepreneurship Cell, KIIT University</p>
  </div>
</div>
</body>
</html>
"""
    plain = Template(plain_template).render(**data)
    html = Template(html_template).render(**data)
    return plain, html
