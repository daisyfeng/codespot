<?php
function the_video_url($post_id) {
  $post = get_post($post_id);
  if(!empty($post)) {
    $content = $post->post_content;
    $r = "/<embed \s.* height=\"\d.*?\" src=\"(\S.*?)\" \S.*?>/i";
    if(preg_match($r,$content,$match))
      print_r($match);
  }
  }
    