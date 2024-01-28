<!-- svelte-ignore a11y-missing-attribute -->
<style>
	html {
  font-family: 'Roboto', sans-serif;
}
  
body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  color: white;
  background: linear-gradient(-45deg, #aac0f4, rgb(163, 161, 255), #c0e6ff, #c3b8fd);
  background-size: 400% 400%;
  animation: gradient 10s ease infinite;
  height: 100vh;
  }
  @keyframes gradient {
    0% {
    background-position: 0% 50%;
    }
    50% {
    background-position: 100% 50%;
    }
    100% {
    background-position: 0% 50%;
    }
}

.outlined-text {
  color: white;
  text-shadow:
    -1px -1px 0 #b9bcfc,
     1px -1px 0 #c9d3ff,
    -1px  1px 0 #bbedff,
     1px  1px 0 #ebfcff;
}

.btn {
  background-color: rgb(112, 112, 186);
  text-align: center;
  padding: 20px;
  border-radius: 15px;
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  padding-left: 10%;
  padding-right: 10%;
  height: 7vh;
  overflow: hidden;
}

nav a img {
  height: 50px;
}

#nav-list {
  list-style: none;
  display: flex;
  margin: 0;
  padding: 0;
  align-items: center;
  justify-content: center;
  flex: 1;
}

#nav-list li {
  padding: 0 15px;
}

#nav-list li a {
  text-decoration: none;
  color: #ffffff;
  padding: 10px;
  border-radius: 10px;
  transition: all 0.3s ease-in-out;
  font-size: 20px;
}

nav .try-now {  
  background-color: rgb(169, 181, 245);
  color: #fff;
  padding: 10px 20px;
  border-radius: 10px;
  text-decoration: none;
  transition: transform 0.2s ease-in;
  }

  nav .try-now:hover {  
    background-color: rgb(121, 217, 255);
    color: #000000;
    transform: scale(1.3);
    box-shadow: 1px 1px 20px rgba(26, 5, 255, 0.9);
  }

.flex-item:hover {
  transform: scale(1.1);
  background-color: #159bfa;
}

  
#nav-list li a:hover {
  background-color: aliceblue;
  color: black;
}
  
.hamburger {
  display: none;
  font-size: 30px;
  cursor: pointer;
}
  
.nav-toggle {
  display: none;
}
 
@media screen and (max-width: 768px) {
  .hamburger {
      display: block;
  }
  
  #nav-list {
      display: none;
      width: 100%;
      flex-direction: column;
      text-align: center;
  }
  
  #nav-list li {
      padding: 10px 0;
  }
  
  .nav-toggle:checked + #nav-list {
      display: flex;
  }
}

.btn1 {
  outline: 0;
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
  background: #159bfa;
  min-width: 200px;
  border: 0;
  border-radius: 4px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, .1);
  box-sizing: border-box;
  padding: 16px 20px;
  color: #fff;
  font-size: 20px;
  font-weight: 600;
  letter-spacing: 1.2px;
  text-transform: uppercase;
  overflow: hidden;
  cursor: pointer;
  text-decoration: none;
  transition: transform 0.2s ease-in;
}

.btn1:hover {
  opacity: .95;
  background-color: rgb(121, 217, 255);
  color: #000000;
  transform: scale(1.3);
  box-shadow: 1px 1px 20px rgba(26, 5, 255, 0.5);
}

.btn1 .animation {
  border-radius: 100%;
  animation: ripple 0.6s linear infinite;
}

@keyframes ripple {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.1), 0 0 0 20px rgba(255, 255, 255, 0.1), 0 0 0 40px rgba(255, 255, 255, 0.1), 0 0 0 60px rgba(255, 255, 255, 0.1);
  }

  100% {
    box-shadow: 0 0 0 20px rgba(255, 255, 255, 0.1), 0 0 0 40px rgba(255, 255, 255, 0.1), 0 0 0 60px rgba(255, 255, 255, 0.1), 0 0 0 80px rgba(255, 255, 255, 0);
  }
}

.presentation {
  text-align: center;
  padding-left: 20%;
  padding-right: 20%;
}

.image-container {
  position: absolute;
  top: 0;
  width: 100%;
  height: 100vh;
  z-index: -1;
  overflow: hidden;
  background-image: url('./Images/grid.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  opacity: 0.1;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(2, 1fr);
  
  margin-left: 30%;
  margin-right: 30%;
  margin-top: 100px;
}

.grid-item {
  border: 1px solid #ddd;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  aspect-ratio: 1;
  margin: 30px;
  background-color: rgb(94, 94, 94, 0.05);
  box-shadow: 10px 1px 20px rgba(84, 84, 84, 0.5);
}



/* ---------------------------------------- CTF.HTML CSS---------------------------------------*/

.form {
  margin-left: 20%;
  margin-right: 20%;
  border-radius: 1;
}

.forminput {
  width: 300px;
  height: 40px;
  border-radius: 10px;
  background-color: rgb(148, 148, 148, 0.1);
}

.forminput::placeholder {
  color: white;
  font-size: 15px;
  text-align: center;
}

.content {
  background-color: rgb(130, 130, 130, 0.1);
  height: 100vh;
  padding: 5%;
  border-radius: 15px;
}


/* ---------------------------------------- ABOUT.HTML CSS---------------------------------------*/
.container {

  flex-direction: row;
}

.flex-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-column-gap: 15px;
}

.flex-item {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 15px;
  margin: 10px;
  background-color: rgb(128, 128, 128, 0.3);
  transition: transform 0.3s ease;
  display: flex;
  justify-content: center;
  align-items: center;
}

.flex-item:hover {
  transform: scale(1.1);
  background-color: #159bfa;
}

.inside {
  background-color: #159bfa;
  height: 250px;
}

.profile-pic {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  text-align: center;
}


.profpic {
  padding: 15px;
}

.name {
  font-size: 20px;
  font-weight: 300;
  text-decoration: none;
  text-align: center;
}

.abouttitle {
  margin-left: 15%; 
  margin-right: 15%; 
  
  text-align: center;
}

.abouttitle h1 {
  font-size: 70px;
}


.abouttext {
  font-size: 40px;
}

.column {
  width: 300px;
  height: 500px;
  border: px solid black;
  border-radius: 20px;
  transition: box-shadow 300ms;
  transition:  300ms;
  background-color: rgba(217, 217, 217, 0.2);
  transition: transform 0.3s ease;
}

.content1 {
  text-align: center;
  margin-top: 40px;
}

.profile {

  width: 150px;
  height: 150px;
  border-radius: 100%;
  margin: 0;
  padding: 0;
}

.text {
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 30px;
  padding-bottom: 30px;
  margin-left: 10px;
  margin-right: 10px;
  border-radius: 20px;
  text-decoration: none;
}

.column:hover {
  cursor: pointer;
	animation: grow 1s;
	animation-fill-mode: forwards;
	position: relative;
	z-index: 50;
  background-color: rgba(69,243,255, 0.7);
  color: #23242a;
}
@keyframes grow {
  to {
      transform: scale(1.2)
  }
}

.text {

}

.text {

}

.text {

}

.text {

}



</style>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="./styles.css" >
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
  <link rel="shortcut icon" type="image/x-icon" href="./Images/logoweb.png" />
  <title>Index</title>
</head>
<body>
  <section>
    <nav>
      <a href="index.html"><img src="./Images/logo.png" alt="Logo"></a>
      
      <ul id="nav-list">
        <li><a href="/ctf" style="box-shadow: 1px 1px 20px rgba(26, 5, 255, 0.3);">Explore</a></li>
        <li><a href="/system">How It Works</a></li>
        <li><a href="/about">About</a></li>
      </ul>
    
      <a href="CTF.html" class="try-now">SEARCH</a>
    </nav>
    <div class="image-container"></div>
  </section>

  <section>
    <div class="presentation">
      <h1 style="font-size:80px; margin-top:10px; margin-bottom:10px; box-shadow: 10px;" class="outlined-text">Welcome to MediQuest AI</h1>
      <h2 style="font-size:30px; margin-top:10px; margin-bottom:10px;" class="outlined-text">Your Gateway to <i>THE</i> Clinical Trial for you</h2>
      <h3 style="text-align: center;">
        We take your health seriously at Clinical Trial Finder. By connecting you with the latest, 
        personalized medical trials, we strive to bring you closer to the care you need, efficiently 
        and reliably.
      </h3>
      <br><br>
      <div>
        <a href="./ctf.html" class="btn1"><i class="animation"></i>TRY US NOW<i class="animation"></i></a>
      </div>
    </div>
  </section>

  <section class="grid-container">
    <div class="grid-item">Free</div>
    <div class="grid-item">Reliable </div>
    <div class="grid-item">Accurate</div>
    <div class="grid-item">4</div>
    <div class="grid-item">5</div>
    <div class="grid-item">6</div>
  </section>
  <footer>
    <!-- Footer content here -->
  </footer>
</body>
</html>
