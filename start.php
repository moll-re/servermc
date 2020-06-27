<html>
   <head>
   </head>

   <body>
     <?php
      $status = 'at rest';
      $hash = '$2y$07$BCryptRequires22Chrcte/VlQH0piJtjXl.0t1XkA8pw9dMXTpOq';

      function check_pw(){
        $pw = $_POST["password"]
        if (password_verify('$pw', $hash)) {
          $status = "SUCCESS";
          shell_exec("server_boot.sh");
      } else {
         $status = "try again";
      }
    }
      ?>
     <h1> Start the MC-Server </h1>

     Reminder: ip adress is: <a href="mc.remy-moll.selfhost.eu">mc.remy-moll.selfhost.eu</a>

     <form method="post" action="check_pw">
       Password: <input type="password" name="password">
       <br/><input type="submit" value="submit" name="submit">
     </form>
     Status: <?php echo $status ?>
   </body>
</html>
