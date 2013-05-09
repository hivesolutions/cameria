{% extends "partials/layout.html.tpl" %}
{% block title %}Accounts{% endblock %}
{% block name %}Accounts :: {{ account.username }}{% endblock %}
{% block content %}
    <div class="quote">{{ account.username }}</div>
    <div class="separator-horizontal"></div>
    <table>
        <tbody>
            <tr>
                <td class="right label" width="50%">tokens</td>
                <td class="left value" width="50%">
                    {% for token in account.tokens %}
                        {{ token }}{% if not loop.last %},{% endif %}
                    {% endfor %}
                </td>
            </tr>
            <tr>
                <td class="right label" width="50%">cameras</td>
                <td class="left value" width="50%">
                    {% if account.cameras == None %}
                        all
                    {% else %}
                        {% for camera in account.cameras.objects %}
                            <a href="{{ url_for('show_camera', camera_id = camera.camera_id) }}">{{ camera }}</a>{% if not loop.last %},{% endif %}
                        {% endfor %}
                    {% endif %}
                </td>
            </tr>
        </tbody>
    </table>
{% endblock %}
