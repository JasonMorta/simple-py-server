//import React from 'react'
import { GoogleLogin } from "react-google-login";


export default function LogOutBtn() {

    const clientId = "467887179455-ac64pkrmv8u1i47ii7sbvj8d89hue4u8.apps.googleusercontent.com"

    const onSuccess = (res) => {
        console.log('[Login Success] currentUser:', res.profileObj);
    };

    const onFailure = (res) => {
        console.log('[Login failed] res:', res);
    }

  return (
    <div id='logoutButton'>
    <GoogleLogin
        clientId={clientId}
        buttonText="Logout"
        onAutoLoadFinished={onSuccess}
        onFailure={onFailure}

        />
</div>
  )
}
