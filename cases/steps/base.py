"""
Horizon base steps.

@author: schipiga@mirantis.com
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class BaseSteps(object):
    """Base steps."""

    def __init__(self, app):
        """Constructor.

        Arguments:
            - app: horizon application instance.
        """
        self.app = app

    def _open(self, page):
        current_page = self.app.current_page
        if page.__class__ != current_page.__class__:

            if getattr(page, 'navigate_items', None):
                current_page.navigate(page.navigate_items)

            else:
                page.open()

        return page
