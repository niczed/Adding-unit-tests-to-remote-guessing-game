from unittest import TestCase
from unittest.mock import patch, MagicMock
from server import start_server  # your original game server code

class TestServerStart(TestCase):

    @patch('random.randint', return_value=42)  # Mocking random number
    @patch('socket.socket')  # Correctly mocking the global socket module
    def test_start_server_with_mocked_socket(self, mock_socket_class, mock_randint):
        mock_socket = MagicMock()
        mock_socket_class.return_value.__enter__.return_value = mock_socket

        mock_conn = MagicMock()
        # Simulated guesses: 30 (too low), 50 (too high), 42 (correct), "" (disconnect)
        mock_conn.recv.side_effect = [b"30", b"50", b"42", b""]
        mock_socket.accept.return_value = (mock_conn, ("127.0.0.1", 12345))

        start_server()  # Call the actual server code

        expected_calls = [b"Too low", b"Too high", b"Correct"]
        actual_calls = [call[0][0] for call in mock_conn.sendall.call_args_list]
        self.assertEqual(expected_calls, actual_calls)