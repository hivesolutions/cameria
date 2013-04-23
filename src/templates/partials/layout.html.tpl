{% include "partials/doctype.html.tpl" %}
<head>
    {% block head %}
        {% include "partials/content_type.html.tpl" %}
        {% include "partials/includes.html.tpl" %}
        <title>Cameria / {% block title %}{% endblock %}</title>
    {% endblock %}
</head>
<body class="ux">
    <div id="overlay" class="overlay"></div>
    <div id="header">
        {% block header %}
            <h1>{% block name %}{% endblock %}</h1>
            <div class="links">
                 {% if acl("index") %}
                    {% if link == "home" %}
                        <a href="{{ url_for('index') }}" class="active">home</a>
                    {% else %}
                        <a href="{{ url_for('index') }}">home</a>
                    {% endif %}
                {% endif %}
                 {% if acl("sets.list") %}
                    //
                    {% if link == "sets" %}
                        <a href="{{ url_for('list_set') }}" class="active">sets</a>
                    {% else %}
                        <a href="{{ url_for('list_set') }}">sets</a>
                    {% endif %}
                {% endif %}
                {% if acl("cameras.list") %}
                    //
                    {% if link == "cameras" %}
                        <a href="{{ url_for('list_camera') }}" class="active">cameras</a>
                    {% else %}
                        <a href="{{ url_for('list_camera') }}">cameras</a>
                    {% endif %}
                {% endif %}
                {% if acl("devices.list") %}
                    //
                    {% if link == "devices" %}
                        <a href="{{ url_for('list_device') }}" class="active">devices</a>
                    {% else %}
                        <a href="{{ url_for('list_device') }}">devices</a>
                    {% endif %}
                {% endif %}
                {% if acl("about") %}
                    //
                    {% if link == "about" %}
                        <a href="{{ url_for('about') }}" class="active">about</a>
                    {% else %}
                        <a href="{{ url_for('about') }}">about</a>
                    {% endif %}
                {% endif %}
            </div>
        {% endblock %}
    </div>
    <div id="content">{% block content %}{% endblock %}</div>
    {% include "partials/footer.html.tpl" %}
</body>
{% include "partials/end_doctype.html.tpl" %}
