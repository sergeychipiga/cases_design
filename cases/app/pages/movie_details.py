"""
------------------
Movie details page
------------------
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

from pom import ui
from selenium.webdriver.common.by import By

from cases.app.pages.base import PageBase

__all__ = [
    'PageMovieDetails',
]


@ui.register_ui(
    label_title=ui.UI(By.CSS_SELECTOR, 'h1[itemprop="name"]'),
    link_year=ui.Link(By.CSS_SELECTOR, '#titleYear > a'),
    label_rating=ui.UI(By.CSS_SELECTOR, '[itemprop="ratingValue"]'))
class PageMovieDetails(PageBase):
    """Page with movie details."""

    url = '/title'
