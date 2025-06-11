import { useState } from 'react'
import './App.css'
import { useEffect } from 'react'

function App() {

  const [data, setData] = useState("")
  useEffect(()=>{
    fetch("http://127.0.0.1:5000/api/home")
    .then((response)=>response.json())
    .then((data)=>console.log(data.message))
  },[])
  return (
    <div>
     <h1>Check the console</h1>   
    </div>
  )
}

export default App

// respone ko json me kiu kiya?
// or jsonify kiu use kiya?
