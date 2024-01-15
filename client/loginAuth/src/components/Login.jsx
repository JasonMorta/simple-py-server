import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import LoginBtn from "./LoginBtn";


function Login({handleShowIframe, handleLogin}) {
  // get form data

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    //get form email
    const email = e.target[0].value;
    console.log("email", email);

    //get form password
    const password = e.target[1].value;
    console.log("password", password);

    // get form remember me
    const remember = e.target[2].checked;

    //send data to server
    const data = {
      email,
      password,
      remember,
    };

    handleLogin(data)

    console.log("data", data);
    // make login request
    await fetch("http://localhost:8080/login", {
      method: "POST",
      credentials: "include", // this is to send cookies and receive cookies from the server
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
       // console.log("data", data);
      })
      .catch((error) => console.error(error));
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Email address</Form.Label>
        <Form.Control type="text" placeholder="Enter email" />
        <Form.Text className="text-muted">
          We&apos;ll never share your email with anyone else.
        </Form.Text>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" placeholder="Password" />
      </Form.Group>
      <Form.Group className="mb-3 remember" controlId="formBasicCheckbox">
        <Form.Check type="checkbox" label="Remember me" />
      </Form.Group>
      <Button variant="secondary" type="submit">
        Login
      </Button>
      <div className="login_options">
      <LoginBtn />
        <Button 
          variant="primary"
          onClick={handleShowIframe}
          >Show iFrame</Button>
      </div>
    </Form>
  );
}

export default Login;
