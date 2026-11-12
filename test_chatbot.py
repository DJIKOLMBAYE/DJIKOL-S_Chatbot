import unittest

from chatbot import FALLBACK_RESPONSE, chatbot_response


class ChatbotResponseTests(unittest.TestCase):
    def test_known_message_ignores_case_and_surrounding_whitespace(self) -> None:
        self.assertEqual(
            chatbot_response("  BONJOUR! "),
            "Bonjour! Comment puis-je vous aider aujourd'hui?",
        )

    def test_unknown_message_returns_fallback(self) -> None:
        self.assertEqual(chatbot_response("une question inconnue"), FALLBACK_RESPONSE)


if __name__ == "__main__":
    unittest.main()
