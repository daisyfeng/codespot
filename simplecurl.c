#include <stdio.h>
#include <curl/curl.h>
#include <curl/types.h>
#include <curl/easy.h>
#include <string.h>

struct vFile {
  const char *filename;
  FILE *stream;
};

static size_t vfwrite(void *buffer, size_t size, size_t nmemb, void *stream) {

  struct vFile *out=(struct vFile *)stream;
  if(out && !out->stream) {
    out->stream=fopen(out->filename, "wb");
    if(!out->stream)
      return -1;
  }
  return fwrite(buffer, size, nmemb, out->stream);
}

void dirp(char *video) {
  char *p;
  char *dir;
  char *t = '';
  int i;
  p = strtok(video,'/');
  for (i = 0,p!=NULL,i++) {
    dir[i] = p;
    p = strtok(NULL,'/');
  }

  for (int k = 0,k < i,k++) {
    t = strcat(dir[k])
    
void err(char *video) {
  FILE *fd;
  fd = fopen("curl.txt", "a+");
      
  if (fd) {
    fputs(video,fd); 
    fclose(fd);
  }
}
        
int main(int argc, char *argv[]) {
  CURL *curl;
  CURLcode res;

  struct vFile vfile ={argv[2],
                       NULL};
  
  curl_global_init(CURL_GLOBAL_DEFAULT);
  
  curl = curl_easy_init();
  if(curl) {
    curl_easy_setopt(curl, CURLOPT_URL,argv[1]);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, vfwrite);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &vfile);  
    curl_easy_setopt(curl, CURLOPT_VERBOSE,0L);  
    res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);
    
    if(CURLE_OK != res) {
      printf("%d",res);
      err(strcat(argv[1],"\n"));}
  }
  if(vfile.stream)
    fclose(vfile.stream);
  curl_global_cleanup();
  
  return 0;
}
