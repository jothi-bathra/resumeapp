function validateHTMlform()
{
  let form = document.register;
   if( form.name.value == "" )
   {
     alert( "Enter Your  Name!" );
     form.textnames.focus() ;
     return;
   }
   if( form.email.value == "" )
   {
     alert( "Enter Your email!" );
     form.textnames.focus() ;
     return;
   }
  
   if( form.pass.value == "" )
   {
     alert( "Enter Your password!" );
     form.fathername.focus() ;
     return;
   }
var email = form.email.value;
  atpos = email.indexOf("@");
  dotpos = email.lastIndexOf(".");
if (email == "" || atpos < 1 || ( dotpos - atpos < 2 ))
{
     alert("Enter your correct email ID")
     form.emailid.focus() ;
     return;
}
  
   return( true );
}