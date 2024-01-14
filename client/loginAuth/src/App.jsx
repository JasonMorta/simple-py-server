//import { useState } from 'react'

import './App.css'
import Login from './components/Login'
import { useEffect } from 'react'
import { gapi } from 'gapi-script'

function App() {

  useEffect(() => {
    function start() {
      gapi.client.init({
        clientId: "467887179455-ac64pkrmv8u1i47ii7sbvj8d89hue4u8.apps.googleusercontent.com",
        scope: "",
      })
    }
    gapi.load("client:auth2", start)
  
   
  })
  
// Get user access token
//   const accessToken = gapi.auth.getToken().access_token

  return (
    <>
    <Login />
    </>
  )
}

export default App
