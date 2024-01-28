<script>
  let text_box = "Please Write your condition";
</script>
<style>

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


.flex-item:hover {
  transform: scale(1.1);
  background-color: #159bfa;
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

.send {
  font-size: 1.2rem;
  padding: 1rem 2.5rem;
  border: none;
  outline: none;
  border-radius: 0.4rem;
  cursor: pointer;
  text-transform: uppercase;
  background-color: rgb(14, 14, 26);
  color: rgb(234, 234, 234);
  font-weight: 700;
  transition: 0.6s;
  box-shadow: 0px 0px 60px #1f4c65;
  -webkit-box-reflect: below 10px linear-gradient(to bottom, rgba(0,0,0,0.0), rgba(0,0,0,0.1));
}

.send:active {
  scale: 0.92;
}

.send:hover {
  background: rgb(2,29,78);
  background: linear-gradient(270deg, rgba(2, 29, 78, 0.681) 0%, rgba(31, 215, 232, 0.873) 60%);
  color: rgb(4, 4, 38);
}

.btn3 {
  display: grid;
  place-items: center;
  height: 100px;
}
</style>


  <section class="form">
    <div class="content">
        <form style="background-color: rgba(255, 255, 255, 0.2); backdrop-filter: blur(5px); padding: 15px; border-radius: 15px; box-shadow: 1px 1px 20px rgba(10, 5, 20, 0.5);">
            <h1 class="outlined-text">MediQuest AI Form</h1>
            <div>
                <label for="notes">To better assist you in finding the most suitable clinical trials, please provide us with 
                    details about your medical condition or diagnosis. The information you share will enable our AI-driven 
                    system to identify and recommend trials that are most relevant to your specific health needs.
                </label> 
                <br><br>
                <textarea style="width: 100%; height: 300px; background-color: rgb(148, 148, 148, 0.1); border-radius: 10px;" bind:value={text_box}/>
                <div class="btn3">
                  <button type="submit" id="submitButton" class="send">
                    SEND
                  </button>
                </div>
                <br><br>
            </div>
            
        </form>
    </div>
  </section>

  

  <footer>
    <!-- Footer content here -->
  </footer>

