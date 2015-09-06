<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Super Uploader 1.0</title>
    <link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script>
      $(document).ready(function() {
        $('#selectFile').on('click', function() { $('#file').trigger('click') });
        $('#file').change(function() { $('#selectedFile').val($(this).val()) });
      });
      // references: http://kuwalab.hatenablog.jp/entry/2014/01/02/191821
    </script>
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <h1>Super Uploader 1.0</h1>
          <p>You can upload any file!</p>
          <form method="post" enctype="multipart/form-data" class="form">
            <input type="file" name="file" id="file" style="display: none;">
            <div class="input-group">
              <input type="text" class="form-control" id="selectedFile" readonly>
              <span class="input-group-btn">
                <button id="selectFile" class="btn btn-defdault" type="button">Select File</button>
              <span>
            </div>
            <input type="submit" value="Upload" class="btn btn-primary">
          </form>

<?php
  if($_SERVER["REQUEST_METHOD"] === "POST") :
?>
<?php
    if (is_uploaded_file($_FILES["file"]["tmp_name"])):
      $file = $_FILES['file'];
      $name = $file['name'];
      if (preg_match("/^[a-zA-Z0-9]+\\.[a-zA-Z0-9]+$/", $name) ):
        $data = file_get_contents($file['tmp_name']);
        while($next = preg_replace("/<\\?/", "", $data)){
          $next = preg_replace("/php/", "", $next);
          if($data === $next) break;
          $data = $next;
        }
        file_put_contents(dirname(__FILE__) . '/u/' . $name, $data);
        chmod(dirname(__FILE__) . '/u/' . $name, 0644);
?>
        <div>
          <a href="<?php echo htmlspecialchars("u/" . $name)?>">Upload successfully!</a>
        </div>
<?php
      endif;
    endif;
?>
<?php
  endif;
?>
        </div>
      </div>
    </div>
  </body>
</htmla>
