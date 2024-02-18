FROM debian:12

# Install packages
RUN apt-get update && apt-get install -y build-essential libexpat1-dev libssl-dev wget vim bash dnsutils

# Download and extract the Unbound source code
RUN wget https://nlnetlabs.nl/downloads/unbound/unbound-1.19.0.tar.gz \
    && tar -xzvf unbound-1.19.0.tar.gz \
    && rm unbound-1.19.0.tar.gz

# Build and install Unbound from the source code
RUN cd unbound-1.19.0 \
    && ./configure \
    && make \
    && make install

# Create unbound user and group
RUN groupadd -r unbound && useradd -r -g unbound unbound

# Run Unbound in the foreground
CMD ["unbound", "-d"]
