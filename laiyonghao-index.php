<?php get_header(); ?>

<!-- 顶部自定义 开始 -->
<div id="topnews">

<div id="txtnews">
    <!-- 将视频代码移至头条判定下部 -->
	 <!-- <div id="picswitch"> -->
 <!-- <embed src="http://player.youku.com/player.php/sid/XMTY0NTY3OTEy/v.swf" quality="high" width="260" height="200" align="middle" allowScriptAccess="sameDomain" type="application/x-shockwave-flash"></embed> -->
 	<!-- </div> -->
 	<!-- 最新头条 开始 -->
	<div id="toplist">
    	<div id="topdetail">
			 <!-- The 1st post, with the black background by default -->
				<?php query_posts('showposts=1&cat=1'); ?>
					<?php while (have_posts()) : the_post(); ?>
						<h4><a href="<?php the_permalink() ?>" title="<?php the_title(); ?>" class="a_blue"><?php the_title(); ?></a></h4>
                        <!-- 寻找最新头条中是否包含类型为video的附件,若存在则将地址赋值给h_video_url -->
                        <?php 
                        $post_id = the_ID();
                        $video = get_children("post_type=attachment&post_mime_type=video&post_parent                                                       =$post_id&numberposts=1");
                        if(is_array($video)) {
                            foreach($video as $att_id => $att) {
                              $h_video_url = wp_get_attachment_link($att_id);
                            }
                        }
                        ?>
						<?php the_excerpt(); ?>
					<?php endwhile; ?>
      	</div>
        	
			<?php query_posts('showposts=5&offset=1&cat=1'); ?><!-- showposts 输出文章的“数目”， “cat=分类ID号”，输出指定分类的文章 -->
            <ul>
               <?php while (have_posts()) : the_post(); ?><!-- Loop 开始 -->
               <li><a href="<?php the_permalink() ?>" rel="bookmark" class="title"><?php the_title(); ?></a>  <?php the_time('Y-m-d'); ?></li><!-- 由上述条件指定的文章标题的列表 -->
               <!-- 以下判定是已否存在video_url,如果不存在则寻找当前头条中的video_url -->
               <?php if(!empty($h_video_url)) {
                         $post_id = the_ID();
                         $video = get_children("post_type=attachment&post_mime_type=video&post_parent                                                       =$post_id&numberposts=1");
                         if(is_array($video)) {
                             foreach($video as $att_id => $att) {
                               $h_video_url = wp_get_attachment_link($att_id);
                             }
                         }
                        }
               ?>
               <!-- 以上判定 -->
               <?php endwhile; ?><!-- Loop 结束 -->
            </ul>
    </div>
    <!-- 最新头条 结束 -->
               
<div id="picswitch">
<embed src="<?php echo empty($h_video_url)?'':$h_video_url;  ?>" quality="high" width="260" height="200" align="middle" allowScriptAccess="sameDomain" type="application/x-shockwave-flash"></embed>
</div>
<!-- 以上测试视频地址动态选择 -->

	<div>
		<li  id="text-3" class="widget widget_text">

		<div class="textwidget">
		<script type="text/javascript"><!--
		google_ad_client = "pub-5923289565184513";
		/* 200x200, 创建于 10-6-26 */
		google_ad_slot = "3499156843";
		google_ad_width = 200;
		google_ad_height = 200;
		//-->
		</script>
		<script type="text/javascript"
		src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
		</script>
		</div>
		</li>
	</div>
</div>
</div>
<!-- 顶部自定义 结束 -->

<!-- 左侧 开始 -->
<div class="con_left">
	<div class="cat-posts">
		<?php include (TEMPLATEPATH . '/cats.php'); ?>
	</div>
</div>
<!-- 左侧 结束 -->

<!-- 右侧 开始 -->
<div class="con_right">
<?php include (TEMPLATEPATH . '/sidebar.php'); ?>
</div>
<!-- 右侧 结束 -->


<?php get_footer(); ?>

</div>
</body>
</html>
