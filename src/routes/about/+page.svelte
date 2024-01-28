<style>
	html {
  font-family: 'Roboto', sans-serif;
}
  
body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  color: white;
  background: linear-gradient(-45deg, #79a1ff, rgb(140, 138, 255), #97b8cf, #afa1f7);
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
  margin-right: 15%;
  margin-left: 15%;
  flex-direction: row;
  display: grid;
  justify-items: center;
}

.flex-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-column-gap: 15px;
  margin-left: 10%;
  margin-right: 10%;
}

.flex-item {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 15px;
  margin: 5px;
  background-color: rgb(128, 128, 128, 0.3);
  transition: transform 0.3s ease;
  display: flex;
  justify-content: center;
  align-items: center;
}

.flex-item:hover {
  transform: scale(1.1);
  background-color: #01487a;
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
</style>

  <section>
    <div class="abouttitle">
        <h1 class="outlined-text"  >ABOUT US</h1>
        <h2>
            <div class="abouttext outlined-text">Passionate About Health and Healing</div>
            <br>
            At <i><b> MediQuest AI</b></i>, our mission is clear: to leverage our expertise in 
            programming and technology to create real-world solutions that help patients find 
            the medical treatments they need. We are a team united by a shared passion for healthcare 
            innovation and the belief that everyone deserves access to the best possible medical care.
        </h2>
        <br><br><br><br>
    </div>    
      <div class="flex-container">
        <div class="column flex-item">
            <a href="https://www.linkedin.com/in/julienhu/" style="text-decoration: none; color:rgb(53, 92, 245)" class="outlined-text">
               <div class="content1">
                  <h3 style="color: aliceblue; font-size: 25px;">Julien Hu</h3>
                  <img class="profile" src="Images/Julien.jpg" style="opacity: 0.8;">
                  <h5 style="text-align: justify; padding: 20px;">
                    Julien is a Computer Science student and a front-end developer with a strong passion 
                    for artificial intelligence. Skilled in creating engaging user interfaces, 
                    he excels in applying innovative AI solutions to enhance web 
                    experiences. 
                    <br><br>
                    Julien combines technical prowess with a creative approach, 
                    constantly exploring new trends in the tech world.
                  </h5>
               </div>
             </a>
         </div>

         <div class="column flex-item">
          <a href="https://www.linkedin.com/in/hayden-choi-56ab23279/" style="text-decoration: none; color:rgb(53, 92, 245)" class="outlined-text">
             <div class="content1">
                <h3 style="color: aliceblue; font-size: 25px;">Hayden Choi</h3>
                <img class="profile" src="Images/hayden.jpg" style="opacity: 0.8;">
                <h5 style="text-align: justify; padding: 20px;">
                  <h5 style="text-align: justify; padding: 20px;">
                    Hayden Choi is a dedicated Computer Science student who has excelled in implementing advanced AI technologies and backend development. His proficiency lies in designing and developing intelligent systems that are both efficient and scalable. 
                    <br><br>
                    With a deep understanding of machine learning algorithms and data structures, Hayden has contributed significantly to the backend aspects of numerous projects. His ability to integrate AI with backend logic has enhanced the functionality and performance of these systems. Hayden's passion for AI and backend development drives him to continuously learn and apply the latest technologies in the field.
                </h5>
                </h5>
             </div>
           </a>
       </div>
       <div class="column flex-item">
        <a href="https://www.linkedin.com/in/julian-laxman/" style="text-decoration: none; color:rgb(53, 92, 245)" class="outlined-text">
           <div class="content1">
              <h3 style="color: aliceblue; font-size: 25px;">Julian Laxman</h3>
              <img class="profile" src="Images/Julian.jpg" style="opacity: 0.8;">
              <h5 style="text-align: justify; padding: 20px;">
                Julien is a Computer Science student and a front-end developer with a strong passion 
                for artificial intelligence. Skilled in creating engaging user interfaces, 
                he excels in applying innovative AI solutions to enhance web 
                experiences. 
                <br><br>
                Julien combines technical prowess with a creative approach, 
                constantly exploring new trends in the tech world.
              </h5>
           </div>
         </a>
     </div>
        <div class="column flex-item">
          <a href="https://www.linkedin.com/in/anthony%2Dboileau%2D0045b5226/" style="text-decoration: none; color:rgb(53, 92, 245)" class="outlined-text">
            <div class="content1">
                <h3 style="color: aliceblue; font-size: 25px;">Anthony Boileau</h3>
                <img class="profile" src="Images/anthony.jpg" style="opacity: 0.8;">
                <h5 style="text-align: justify; padding: 20px;">
                  Julien is a Computer Science student and a front-end developer with a strong passion 
                  for artificial intelligence. Skilled in creating engaging user interfaces, 
                  he excels in applying innovative AI solutions to enhance web 
                  experiences. 
                  <br><br>
                  Julien combines technical prowess with a creative approach, 
                  constantly exploring new trends in the tech world.
                </h5>
            </div>
          </a>
      </div>
      </div>
  </section>

  

  <footer>
    <!-- Footer content here -->
  </footer>

