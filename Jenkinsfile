import jenkins.model.*
import hudson.model.*
import groovy.json.JsonSlurper
import java.util.stream.Collectors
import static java.util.Collections.emptyList
import static java.util.Objects.nonNull
import static java.util.stream.Collectors.toList
import java.util.stream.Collectors



 def cCheckoutPullRequest1 (gitURL, gitRepository) {
  try {
    retry(2) {
      cleanWs()
      sh "git clone --single-branch --branch ${env.CHANGE_TARGET} --depth=5 ${gitURL} ."
    }
  } catch(err) {
      throw err
  }
}

 def cMergePullRequest1 (gitURL, gitRepository ) {
  try {
    sh "git fetch --no-tags --progress ${gitURL} +refs/pull-requests/${env.CHANGE_ID}/from:refs/remotes/origin/${env.BRANCH_NAME}"
    sh "git merge remotes/origin/${env.BRANCH_NAME}"
  } catch(err) {
    throw err
  }
 }

  node ("jenkins_swarm_slave") {

    try {
      stage ('CHECKOUT') {

          println '****** Started CHECKOUT stage ******'
          cCheckoutPullRequest1(  "https://github.com/ElviraBost/multibranch.git" , "multibranch"  )
          println '****** Finisheded CHECKOUT stage ******'
      }
      stage ('MERGE') {
          println '****** Started MERGE stage ******'
          cMergePullRequest1( "https://github.com/ElviraBost/multibranch.git" , "multibranch" )
          println '****** Finisheded MERGE stage ******'
      }

    }catch(e){
      throw e
    }finally {
      cleanWs()
      }
}