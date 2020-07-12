# I'm creating my custom asterisk PBX docker image based on Ubuntu 20.04

###########################################
LABEL maintainer="Christophe@Langenberg.be"
###########################################

FROM ubuntu:20.04

# environmentvariables used only during the build of the image, they are not persistent.
ARG DEBIAN_FRONTEND=noninteractive
ARG ASTERISK_VERSION=17

# install prerequisites
RUN apt-get update && \
    apt-get install -y \
                    build-essential \
                    wget \
                    libssl-dev \
                    libncurses5-dev \
                    libnewt-dev \
                    libxml2-dev \
                    libsqlite3-dev \
                    uuid-dev

RUN wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-${ASTERISK_VERSION}-current.tar.gz && \
    tar -xvf asterisk-${ASTERISK_VERSION}-current.tar.gz && \
    rm asterisk-${ASTERISK_VERSION}-current.tar.gz



# for the port EXPOSE part, you need to keep in mind that 1 asterisk call uses 2 ports (so have a large enough range provisioned!)

## TODO: continue creating this image