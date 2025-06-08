'use client'
import { useEffect, useState } from "react";

export default function Home() {
  const [clientSide, setClientSide] = useState(true);
  const [message, setMessage] = useState("loading")
  const [people, setPeople] = useState([])

  useEffect(()=>{
    fetch("http://127.0.0.1:8080/api/home")
    .then((res)=>res.json())
    .then((data)=>{
      setMessage(data.message)
      setPeople(data.people)
    })
  },[]);

  return (
  <div>
    {clientSide &&
    <div>
     <h1>{message}</h1>
     <ul>
      {people.map((name,index)=>(
        <li key={index} >{name}</li>
      ))}
     </ul>
     </div>
     }

  </div>
  );
}
