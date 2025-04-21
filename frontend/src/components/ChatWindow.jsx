function ChatWindow({ question, setQuestion, handleAsk, answer }) {
    return (
      <div className="flex flex-col items-center">
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask me anything..."
          className="border p-2 mb-2 w-80"
        />
        <button onClick={handleAsk} className="bg-blue-500 text-white px-4 py-2 rounded">
          Ask
        </button>
        {answer && (
          <div className="border p-4 mt-4 w-80 bg-gray-100 rounded">
            <strong>Answer:</strong> {answer}
          </div>
        )}
      </div>
    );
  }
  
  export default ChatWindow;
  