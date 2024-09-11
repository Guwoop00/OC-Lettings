deploy:
    docker build -t yourdockerhubuser/oc_lettings_site:$(GIT_COMMIT_HASH) .
    docker push yourdockerhubuser/oc_lettings_site:$(GIT_COMMIT_HASH)