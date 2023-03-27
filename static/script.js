
big_infos=document.querySelectorAll(".big_info")
line_info=document.querySelector(".line_info")
section_info=document.querySelector(".section_info")
button_bottom=document.querySelector(".button_bottom")
bottom_back=document.querySelector(".bottom_back")
info_text = document.querySelector(".info_text")
text=document.querySelector(".text")
let big_info;

big_infos.forEach(big_info => {

    big_info.addEventListener("click",()=>{

      text=big_info.querySelector(".text")
      num=big_info.querySelector(".number")
      notNum=big_info.querySelector(".about_text")

      let firstPageData = text.textContent

      bottom_back.classList.remove("none")
      button_bottom.classList.add("none")

       
      if (!( num == undefined)) {

      info_text.classList.add("none") 
   
      localStorage.setItem("secondPageData", firstPageData);
      window.location.href = "./theme.html";
     
      }
      else{

        section_info.classList.remove("none")
        line_info.classList.add("none")
      }
 })
 
});


bottom_back.addEventListener('click',()=>{
  location.reload()
  
})
