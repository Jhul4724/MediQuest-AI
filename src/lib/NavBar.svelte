<section>
    <nav>
      <a href="../"><img src="/Images/logo.png" alt="Logo"></a>
      
      <ul id="nav-list">
        <li><a href="../">Explore</a></li>
        <li><a href="/system">How It Works</a></li>
        <li><a href="/about">About</a></li>
      </ul>
    
      <a href="/ctf" class="try-now">SEARCH</a>
    </nav>
    <div class="image-container"></div>
  </section>

  <style>
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

.hamburger {
  display: none;
  font-size: 30px;
  cursor: pointer;
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

.nav-toggle {
  display: none;
}
  
#nav-list li a:hover {
  background-color: aliceblue;
  color: black;
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
  </style>