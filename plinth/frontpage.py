#
# This file is part of Plinth.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Manage application shortcuts on front page.
"""

shortcuts = []


def get_shortcuts():
    """Return menu items in sorted order according to current locale."""
    return sorted(shortcuts, key=lambda x: x['label'])


def add_shortcut(app, label, url, icon, details=None):
    """Add shortcut to front page."""
    shortcuts.append({
        'app': app,
        'label': label,
        'url': url,
        'icon': icon,
        'details': details,
    })


def remove_shortcut(app):
    """
    Remove shortcut from front page.

    If app ends with *, remove all shortcuts with that prefix.
    """
    match = lambda x: x['app'] == app
    if app[-1] == '*':
        match = lambda x: x['app'].startswith(app[:-1])

    shortcuts[:] = [shortcut for shortcut in shortcuts if not match(shortcut)]