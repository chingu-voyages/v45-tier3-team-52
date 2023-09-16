import { useState, useEffect,useRef } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";



export default function BuySellForm (){
    const dispatch= useDispatch()
    
    const handleCLick = async (e) =>{
        e.preventDefault

    }

    return (
        <button onClick={()=>handleClick()} >Save</button>
    )
}