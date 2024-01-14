//import React from 'react'
import { GoogleLogin } from "react-google-login";
import { gapi } from "gapi-script";

export default function LoginBtn() {
  const clientId =
    "467887179455-ac64pkrmv8u1i47ii7sbvj8d89hue4u8.apps.googleusercontent.com";

  const onSuccess = (res) => {
    alert(`Logged in successfully welcome ${res.profileObj.name} 😍.`);
    console.log("[Login Success] currentUser:", res.profileObj);

    const accessToken = gapi.auth.getToken().access_token
    console.log('accessToken', accessToken)
  };

  const onFailure = (res) => {
    console.log("[Login failed] res:", res);
  };

  return (
    <div id="loginButton">
      <GoogleLogin
        clientId={clientId}
        buttonText="Login"
        onSuccess={onSuccess}
        onFailure={onFailure}
        cookiePolicy={"single_host_origin"}
        isSignedIn={true}
      />
    </div>
  );
}
