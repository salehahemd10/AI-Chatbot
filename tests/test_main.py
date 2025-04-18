import unittest
from unittest.mock import patch
from main import main

class TestChatbot(unittest.TestCase):
    
    @patch('main.st')
    def test_response_generation(self, mock_st):
        test_input = "What is earthquake?"
        mock_st.session_state = {"messages": []}
        mock_st.text_input.return_value = test_input
        
        with patch('main.ChatGoogleGenerativeAI') as mock_llm:
            mock_llm.return_value.predict.return_value = "Test response"
            main(api_key="test_key", template="test template")
            
        self.assertTrue(len(mock_st.session_state.messages) > 0)

if __name__ == '__main__':
    unittest.main()
