def set_tag(self, project, repository, tag_name, commit_revision, description=None):
        """
        Creates a tag using the information provided in the {@link RestCreateTagRequest request}
        The authenticated user must have REPO_WRITE permission for the context repository to call this resource.
        :param project:
        :param repository:
        :param tag_name:
        :param commit_revision: commit hash
        :param description: OPTIONAL:
        :return:
        """
        if not self.cloud:
            url = 'rest/api/1.0/projects/{project}/repos/{repository}/tags'.format(project=project,
                                                                                   repository=repository)
        else:
            url = 'rest/api/2.0/projects/{project}/repos/{repository}/tags'.format(project=project,
                                                                                   repository=repository)
        body = {}
        if tag_name is not None:
            body['name'] = tag_name
        elif tag_name is not None:
            body['startPoint'] = commit_revision
        if tag_name is not None:
            body['message'] = description
        return self.post(url, data=body)