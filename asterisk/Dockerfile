# I'm creating my custom asterisk PBX docker image based on Ubuntu 20.04
FROM ubuntu:20.04
LABEL maintainer="Christophe@Langenberg.be" version="0.1"

# environmentvariables used only during the build of the image, they are not persistent.
# DO NOT REMOVE THE FOLLOWING LINE!!! Else the docker image will freeze during the build process
ARG DEBIAN_FRONTEND=noninteractive
# The asterisk version to be installed:
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
                    uuid-dev \
                    git \
                    curl \
                    subversion \
                    libjansson-dev

WORKDIR /usr/src/

# download the asterisk source code
RUN wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-${ASTERISK_VERSION}-current.tar.gz

# catch the name of the unpacked asterisk directory and assign it to a variable:
# ASTERISK_DIR=$(tar -f asterisk-${ASTERISK_VERSION}-current.tar.gz -t | head -n 1)
# and installing some prereq's + launching the config
RUN ASTERISK_DIR=$(tar -f asterisk-${ASTERISK_VERSION}-current.tar.gz -t | head -n 1) && \
    tar -xvf asterisk-${ASTERISK_VERSION}-current.tar.gz && \
    cd $ASTERISK_DIR && \
    contrib/scripts/get_mp3_source.sh && \
    contrib/scripts/install_prereq install && \
    ./configure

# copy the file created when using the terminal gui tool; it contains the addons, etc.
COPY ./make/menuselect.makeopts /usr/src/


# compiling the source code with a custom config
RUN ASTERISK_DIR=$(tar -f asterisk-${ASTERISK_VERSION}-current.tar.gz -t | head -n 1) && \
    mv menuselect.makeopts $ASTERISK_DIR && \
    cd $ASTERISK_DIR && \
    make && \
    make install && \
    make samples && \
    make config && \
    ldconfig && \
    rm ../asterisk-${ASTERISK_VERSION}-current.tar.gz

# copy asterisk config files
COPY ./init/asterisk /etc/default/
COPY ./init/asterisk.conf /etc/asterisk/

# create the asterisk user, without a homedirectory + assigning the needed groups & changing the owner for all asterisk
# related directories
RUN useradd -M asterisk && \
    usermod -aG audio,dialout asterisk && \
    chown -R asterisk:asterisk  /etc/asterisk \
                                /var/lib/asterisk \
                                /var/log/asterisk \
                                /var/spool/asterisk \
                                /usr/lib/asterisk

# Lock the account to prevent logging in:
#RUN usermod -L asterisk

## TODO: for the port EXPOSE part, you need to keep in mind that 1 asterisk call uses 2 ports (so have a large enough range provisioned!)
# expose all ports needed for asterisk
EXPOSE 80 8080 5060 5061

#CMD ['systemctl', 'start', 'asterisk']
USER asterisk
WORKDIR /usr/sbin
CMD ['asterisk','-f']

#VOLUME ["/mnt/development"]



## TODO: continue creating/improving this image
## TODO: make the image smaler (cleanup apt cache stuff, etc.)