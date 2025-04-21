import { useState } from "react";
import ChatWindow from "./components/ChatWindow";
import { askQuestion, uploadDocument } from "./api";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleAsk = async () => {
    const response = await askQuestion(question);
    setAnswer(response.answer);
  };

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    await uploadDocument(file);
    alert("Document uploaded successfully!");
  };

  return (
    <div className="p-4 flex flex-col items-center">
      <h1 className="text-2xl mb-4 font-bold">Agentic AI Assistant</h1>
      <input type="file" onChange={handleUpload} className="mb-4" />
      <ChatWindow
        question={question}
        setQuestion={setQuestion}
        handleAsk={handleAsk}
        answer={answer}
      />
    </div>
  );
}

export default App;
