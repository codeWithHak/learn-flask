import { useState } from 'react'
import './App.css'
import { useEffect } from 'react'

function App() {

  const [data, setData] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const [input, setInput] = useState("")


  const handleSubmit = async (e)=>{
    e.preventDefault()
    setIsLoading(true)

  try {
      const response = await fetch("http://127.0.0.1:5000/api/home",{
        method:"POST",
        headers:{
          "Content-Type":"application/json"
        },
        body:JSON.stringify({user_input:input})
    })

      const result = await response.json()
      const message = result.message
      setData(message)
    } catch (err){
      setData("Error fetching response")
      console.log(err);
      
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
      <input
        name='user_input'
        style={{borderRadius:"5px", padding:"4px", fontSize:"20px"}}
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}/>
      <button type='submit'>Submit</button>
      </form>

     {isLoading ? "Loading.." : data}
        
    </div>
  )
}

export default App

