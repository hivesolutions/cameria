<div id="footer">
    {% block footer %}
        &copy; Copyright 2008-2012 by <a href="http://hive.pt">Hive Solutions</a>.<br />
        {% if session.username %}<a href="#">{{ session.username }}</a> // <a href="{{ url_for('logout') }}">logout</a><br />{% endif %}
    {% endblock %}
</div>
