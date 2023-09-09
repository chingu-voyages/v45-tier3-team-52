import { useState, useEffect,useRef } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";



export default function BuySellForm (){
    const dispatch= useDispatch()
    
    const handleClick = async () =>{
       
        const request = await fetch('http://127.0.0.1:5000/api/auth/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
        email:'cantuk0@harvard.edu',
        password:'zF8*wiaMl'
    }),
  });

  if (request.ok) {
    const data = await request.json();
    console.log('-------->',data)
    return data
    }
}

    return (
        <button onClick={handleClick} >Save</button>
    )
}