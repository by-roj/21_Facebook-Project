# ubuntu 20.04
FROM nginx:stable

RUN apt-get update

# -g : 백그라운드에서 실행
CMD ["nginx", "-g", "daemon off;"]

# 80(http) / 443(https) -443이 보안
EXPOSE 80