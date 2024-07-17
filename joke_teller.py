"""
Joke Telling Module
"""

import pyjokes

class JokeTeller:
    def tell_joke(self):
        return pyjokes.get_joke()
