deploy:
    docker build -t guwoop/oc_lettings_site:$(GIT_COMMIT_HASH) .
    docker push guwoop/oc_lettings_site:$(GIT_COMMIT_HASH)